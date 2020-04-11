/**
 * ACTION TYPES
 */
const GET_USER = 'GET_USER'

/**
 * INITIAL STATE
 */
const defaultUser = {chips: 1000}

/**
 * ACTION CREATORS
 */
const getUser = user => ({type: GET_USER, user})

/**
 * THUNK CREATORS
 */
export const me = () => dispatch => {
  try {
    dispatch(getUser(defaultUser))
  } catch (err) {
    console.error(err)
  }
}

/**
 * REDUCER
 */
export default function(state = defaultUser, action) {
  switch (action.type) {
    case GET_USER:
      return action.user
    default:
      return state
  }
}
