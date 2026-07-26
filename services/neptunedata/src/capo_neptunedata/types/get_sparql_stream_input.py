"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetSparqlStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.encoding
    import capo_neptunedata.types.iterator_type


class GetSparqlStreamInput(TypedDict, closed=True):
    limit: NotRequired["int"]
    """<p>Specifies the maximum number of records to return. There is also a size limit of 10 MB on the response that can't be modified and that takes precedence over the number of records specified in the <code>limit</code> parameter. The response does include a threshold-breaching record if the 10 MB limit was reached.</p> <p>The range for <code>limit</code> is 1 to 100,000, with a default of 10.</p>"""
    iterator_type: NotRequired["capo_neptunedata.types.iterator_type.IteratorType"]
    """<p>Can be one of:</p> <ul> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Indicates that reading should start from the event sequence number specified jointly by the <code>commitNum</code> and <code>opNum</code> parameters.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Indicates that reading should start right after the event sequence number specified jointly by the <code>commitNum</code> and <code>opNum</code> parameters.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Indicates that reading should start at the last untrimmed record in the system, which is the oldest unexpired (not yet deleted) record in the change-log stream.</p> </li> <li> <p> <code>LATEST</code> - Indicates that reading should start at the most recent record in the system, which is the latest unexpired (not yet deleted) record in the change-log stream.</p> </li> </ul>"""
    commit_num: NotRequired["int"]
    """<p>The commit number of the starting record to read from the change-log stream. This parameter is required when <code>iteratorType</code> is<code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>, and ignored when <code>iteratorType</code> is <code>TRIM_HORIZON</code> or <code>LATEST</code>.</p>"""
    op_num: NotRequired["int"]
    """<p>The operation sequence number within the specified commit to start reading from in the change-log stream data. The default is <code>1</code>.</p>"""
    encoding: NotRequired["capo_neptunedata.types.encoding.Encoding"]
    """<p>If set to TRUE, Neptune compresses the response using gzip encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSparqlStreamInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSparqlStreamInput:
    out: GetSparqlStreamInput = {}  # type: ignore[typeddict-item]
    return out
