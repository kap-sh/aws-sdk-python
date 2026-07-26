"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier
    import capo_m2.types.string200


class GetDataSetDetailsRequest(TypedDict, closed=True):
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application that this data set is associated with.</p>"""
    data_set_name: "capo_m2.types.string200.String200"
    """<p>The name of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSetDetailsRequest:
    out: GetDataSetDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
