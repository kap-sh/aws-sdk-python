"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetLoaderJobStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.positive_integer


class GetLoaderJobStatusInput(TypedDict, closed=True):
    load_id: "str"
    """<p>The load ID of the load job to get the status of.</p>"""
    details: NotRequired["bool"]
    """<p>Flag indicating whether or not to include details beyond the overall status (<code>TRUE</code> or <code>FALSE</code>; the default is <code>FALSE</code>).</p>"""
    errors: NotRequired["bool"]
    """<p>Flag indicating whether or not to include a list of errors encountered (<code>TRUE</code> or <code>FALSE</code>; the default is <code>FALSE</code>).</p> <p>The list of errors is paged. The <code>page</code> and <code>errorsPerPage</code> parameters allow you to page through all the errors.</p>"""
    page: NotRequired["aws_sdk_neptunedata.types.positive_integer.PositiveInteger"]
    """<p>The error page number (a positive integer; the default is <code>1</code>). Only valid when the <code>errors</code> parameter is set to <code>TRUE</code>.</p>"""
    errors_per_page: NotRequired[
        "aws_sdk_neptunedata.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of errors returned in each page (a positive integer; the default is <code>10</code>). Only valid when the <code>errors</code> parameter set to <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLoaderJobStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLoaderJobStatusInput:
    out: GetLoaderJobStatusInput = {}  # type: ignore[typeddict-item]
    return out
