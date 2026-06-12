"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataPartitionUploadOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.event_expression
    import aws_sdk_iotfleetwise.types.language_version


class DataPartitionUploadOptions(TypedDict):
    expression: "aws_sdk_iotfleetwise.types.event_expression.eventExpression"
    """<p>The logical expression used to recognize what data to collect. For example, <code>$variable.`Vehicle.OutsideAirTemperature` &gt;= 105.0</code>.</p>"""
    condition_language_version: NotRequired[
        "aws_sdk_iotfleetwise.types.language_version.languageVersion"
    ]
    """<p>The version of the condition language. Defaults to the most recent condition language version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPartitionUploadOptions) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    if "condition_language_version" in value:
        out["conditionLanguageVersion"] = value["condition_language_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataPartitionUploadOptions:
    out: DataPartitionUploadOptions = {}  # type: ignore[typeddict-item]
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("DataPartitionUploadOptions.expression required")
    if "conditionLanguageVersion" in data:
        out["condition_language_version"] = data["conditionLanguageVersion"]
    return out
