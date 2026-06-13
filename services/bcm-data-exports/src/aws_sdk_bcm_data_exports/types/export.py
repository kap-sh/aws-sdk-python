"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#Export``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.data_query
    import aws_sdk_bcm_data_exports.types.destination_configurations
    import aws_sdk_bcm_data_exports.types.export_name
    import aws_sdk_bcm_data_exports.types.generic_string
    import aws_sdk_bcm_data_exports.types.refresh_cadence


class Export(TypedDict):
    export_arn: NotRequired["aws_sdk_bcm_data_exports.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    name: "aws_sdk_bcm_data_exports.types.export_name.ExportName"
    """<p>The name of this specific data export.</p>"""
    description: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The description for this specific data export.</p>"""
    data_query: "aws_sdk_bcm_data_exports.types.data_query.DataQuery"
    """<p>The data query for this specific data export.</p>"""
    destination_configurations: "aws_sdk_bcm_data_exports.types.destination_configurations.DestinationConfigurations"
    """<p>The destination configuration for this specific data export.</p>"""
    refresh_cadence: "aws_sdk_bcm_data_exports.types.refresh_cadence.RefreshCadence"
    """<p>The cadence for Amazon Web Services to update the export in your S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Export) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_bcm_data_exports.types.data_query

    out["DataQuery"] = aws_sdk_bcm_data_exports.types.data_query.serialize_aws_json_1_1(
        value["data_query"]
    )
    import aws_sdk_bcm_data_exports.types.destination_configurations

    out["DestinationConfigurations"] = (
        aws_sdk_bcm_data_exports.types.destination_configurations.serialize_aws_json_1_1(
            value["destination_configurations"]
        )
    )
    import aws_sdk_bcm_data_exports.types.refresh_cadence

    out["RefreshCadence"] = (
        aws_sdk_bcm_data_exports.types.refresh_cadence.serialize_aws_json_1_1(
            value["refresh_cadence"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Export:
    out: Export = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Export.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "DataQuery" in data:
        import aws_sdk_bcm_data_exports.types.data_query

        out["data_query"] = (
            aws_sdk_bcm_data_exports.types.data_query.deserialize_aws_json_1_1(
                data["DataQuery"]
            )
        )
    else:
        raise DeserializationError("Export.data_query required")
    if "DestinationConfigurations" in data:
        import aws_sdk_bcm_data_exports.types.destination_configurations

        out["destination_configurations"] = (
            aws_sdk_bcm_data_exports.types.destination_configurations.deserialize_aws_json_1_1(
                data["DestinationConfigurations"]
            )
        )
    else:
        raise DeserializationError("Export.destination_configurations required")
    if "RefreshCadence" in data:
        import aws_sdk_bcm_data_exports.types.refresh_cadence

        out["refresh_cadence"] = (
            aws_sdk_bcm_data_exports.types.refresh_cadence.deserialize_aws_json_1_1(
                data["RefreshCadence"]
            )
        )
    else:
        raise DeserializationError("Export.refresh_cadence required")
    return out
