"""Generated from Smithy shape ``com.amazonaws.quicksight#RollingDateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_identifier
    import aws_sdk_quicksight.types.expression


class RollingDateConfiguration(TypedDict):
    data_set_identifier: NotRequired[
        "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    ]
    """<p>The data set that is used in the rolling date configuration.</p>"""
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The expression of the rolling date configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollingDateConfiguration) -> dict:
    out: dict = {}
    if "data_set_identifier" in value:
        out["DataSetIdentifier"] = value["data_set_identifier"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> RollingDateConfiguration:
    out: RollingDateConfiguration = {}  # type: ignore[typeddict-item]
    if "DataSetIdentifier" in data:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("RollingDateConfiguration.expression required")
    return out
