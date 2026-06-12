"""Generated from Smithy shape ``com.amazonaws.forecast#CreateExplainabilityExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.data_destination
    import aws_sdk_forecast.types.format
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.tags


class CreateExplainabilityExportRequest(TypedDict):
    explainability_export_name: "aws_sdk_forecast.types.name.Name"
    """<p>A unique name for the Explainability export.</p>"""
    explainability_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Explainability to export.</p>"""
    destination: "aws_sdk_forecast.types.data_destination.DataDestination"
    tags: NotRequired["aws_sdk_forecast.types.tags.Tags"]
    """<p>Optional metadata to help you categorize and organize your resources. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>"""
    format: NotRequired["aws_sdk_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExplainabilityExportRequest) -> dict:
    out: dict = {}
    out["ExplainabilityExportName"] = value["explainability_export_name"]
    out["ExplainabilityArn"] = value["explainability_arn"]
    import aws_sdk_forecast.types.data_destination

    out["Destination"] = aws_sdk_forecast.types.data_destination.serialize_aws_json_1_1(
        value["destination"]
    )
    if "tags" in value:
        import aws_sdk_forecast.types.tags

        out["Tags"] = aws_sdk_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExplainabilityExportRequest:
    out: CreateExplainabilityExportRequest = {}  # type: ignore[typeddict-item]
    if "ExplainabilityExportName" in data:
        out["explainability_export_name"] = data["ExplainabilityExportName"]
    else:
        raise DeserializationError(
            "CreateExplainabilityExportRequest.explainability_export_name required"
        )
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
    else:
        raise DeserializationError(
            "CreateExplainabilityExportRequest.explainability_arn required"
        )
    if "Destination" in data:
        import aws_sdk_forecast.types.data_destination

        out["destination"] = (
            aws_sdk_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateExplainabilityExportRequest.destination required"
        )
    if "Tags" in data:
        import aws_sdk_forecast.types.tags

        out["tags"] = aws_sdk_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "Format" in data:
        out["format"] = data["Format"]
    return out
