"""Generated from Smithy shape ``com.amazonaws.location#DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.intended_use


class DataSourceConfiguration(TypedDict, closed=True):
    intended_use: NotRequired["aws_sdk_location.types.intended_use.IntendedUse"]
    """<p>Specifies how the results of an operation will be stored by the caller. </p> <p>Valid values include:</p> <ul> <li> <p> <code>SingleUse</code> specifies that the results won't be stored. </p> </li> <li> <p> <code>Storage</code> specifies that the result can be cached or stored in a database.</p> </li> </ul> <p>Default value: <code>SingleUse</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    if "intended_use" in value:
        out["IntendedUse"] = value["intended_use"]
    return out


def deserialize_json(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "IntendedUse" in data:
        out["intended_use"] = data["IntendedUse"]
    return out
