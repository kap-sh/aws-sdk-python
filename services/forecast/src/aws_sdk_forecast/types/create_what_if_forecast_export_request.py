"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfForecastExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.data_destination
    import aws_sdk_forecast.types.format
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.tags
    import aws_sdk_forecast.types.what_if_forecast_arn_list_for_export


class CreateWhatIfForecastExportRequest(TypedDict):
    what_if_forecast_export_name: "aws_sdk_forecast.types.name.Name"
    """<p>The name of the what-if forecast to export.</p>"""
    what_if_forecast_arns: "aws_sdk_forecast.types.what_if_forecast_arn_list_for_export.WhatIfForecastArnListForExport"
    """<p>The list of what-if forecast Amazon Resource Names (ARNs) to export.</p>"""
    destination: "aws_sdk_forecast.types.data_destination.DataDestination"
    """<p>The location where you want to save the forecast and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3 bucket.</p> <p>If encryption is used, <code>Destination</code> must include an Key Management Service (KMS) key. The IAM role must allow Amazon Forecast permission to access the key.</p>"""
    tags: NotRequired["aws_sdk_forecast.types.tags.Tags"]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html\">tags</a> to apply to the what if forecast.</p>"""
    format: NotRequired["aws_sdk_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfForecastExportRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastExportName"] = value["what_if_forecast_export_name"]
    import aws_sdk_forecast.types.what_if_forecast_arn_list_for_export

    out["WhatIfForecastArns"] = (
        aws_sdk_forecast.types.what_if_forecast_arn_list_for_export.serialize_aws_json_1_1(
            value["what_if_forecast_arns"]
        )
    )
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


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfForecastExportRequest:
    out: CreateWhatIfForecastExportRequest = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastExportName" in data:
        out["what_if_forecast_export_name"] = data["WhatIfForecastExportName"]
    else:
        raise DeserializationError(
            "CreateWhatIfForecastExportRequest.what_if_forecast_export_name required"
        )
    if "WhatIfForecastArns" in data:
        import aws_sdk_forecast.types.what_if_forecast_arn_list_for_export

        out["what_if_forecast_arns"] = (
            aws_sdk_forecast.types.what_if_forecast_arn_list_for_export.deserialize_aws_json_1_1(
                data["WhatIfForecastArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWhatIfForecastExportRequest.what_if_forecast_arns required"
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
            "CreateWhatIfForecastExportRequest.destination required"
        )
    if "Tags" in data:
        import aws_sdk_forecast.types.tags

        out["tags"] = aws_sdk_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "Format" in data:
        out["format"] = data["Format"]
    return out
