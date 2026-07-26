"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.import_destinations
    import capo_cloudtrail.types.import_status
    import capo_cloudtrail.types.uuid


class ImportsListItem(TypedDict, closed=True):
    import_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p> The ID of the import. </p>"""
    import_status: NotRequired["capo_cloudtrail.types.import_status.ImportStatus"]
    """<p> The status of the import. </p>"""
    destinations: NotRequired[
        "capo_cloudtrail.types.import_destinations.ImportDestinations"
    ]
    """<p> The ARN of the destination event data store. </p>"""
    created_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> The timestamp of the import's creation. </p>"""
    updated_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> The timestamp of the import's last update. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportsListItem) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["ImportId"] = value["import_id"]
    if "import_status" in value:
        import capo_cloudtrail.types.import_status

        out["ImportStatus"] = (
            capo_cloudtrail.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "destinations" in value:
        import capo_cloudtrail.types.import_destinations

        out["Destinations"] = (
            capo_cloudtrail.types.import_destinations.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "created_timestamp" in value:
        import capo_cloudtrail.types.date

        out["CreatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_cloudtrail.types.date

        out["UpdatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportsListItem:
    out: ImportsListItem = {}  # type: ignore[typeddict-item]
    if "ImportId" in data:
        out["import_id"] = data["ImportId"]
    if "ImportStatus" in data:
        import capo_cloudtrail.types.import_status

        out["import_status"] = (
            capo_cloudtrail.types.import_status.deserialize_aws_json_1_1(
                data["ImportStatus"]
            )
        )
    if "Destinations" in data:
        import capo_cloudtrail.types.import_destinations

        out["destinations"] = (
            capo_cloudtrail.types.import_destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["created_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreatedTimestamp"]
        )
    if "UpdatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["updated_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["UpdatedTimestamp"]
        )
    return out
