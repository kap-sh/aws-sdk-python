"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetWorkUnitResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.result_stream


class GetWorkUnitResultsResponse(TypedDict, closed=True):
    result_stream: "capo_lakeformation.types.result_stream.ResultStream"
    """<p>Rows returned from the <code>GetWorkUnitResults</code> operation as a stream of Apache Arrow v1.0 messages.</p>"""
