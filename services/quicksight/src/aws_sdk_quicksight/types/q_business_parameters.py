"""Generated from Smithy shape ``com.amazonaws.quicksight#QBusinessParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.application_arn


class QBusinessParameters(TypedDict, closed=True):
    application_arn: "aws_sdk_quicksight.types.application_arn.ApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QBusinessParameters) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> QBusinessParameters:
    out: QBusinessParameters = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError("QBusinessParameters.application_arn required")
    return out
