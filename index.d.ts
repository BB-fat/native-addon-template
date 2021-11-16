/**
 * Add A and B async.
 * @param {number} a
 * @param {number} b
 * @returns {Promise<number>}
 * @see addSync
 */
export function add(a: number, b: number): Promise<number>;

/**
 * Add A and B sync.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 * @see add
 */
export function addSync(a: number, b: number): number;