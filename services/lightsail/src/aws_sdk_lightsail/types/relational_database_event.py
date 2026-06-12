"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.string_list


class RelationalDatabaseEvent(TypedDict):
    resource: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The database that the database event relates to.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the database event was created.</p>"""
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The message of the database event.</p>"""
    event_categories: NotRequired["aws_sdk_lightsail.types.string_list.StringList"]
    """<p>The category that the database event belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseEvent) -> dict:
    out: dict = {}
    if "resource" in value:
        out["resource"] = value["resource"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "event_categories" in value:
        import aws_sdk_lightsail.types.string_list

        out["eventCategories"] = (
            aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseEvent:
    out: RelationalDatabaseEvent = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "message" in data:
        out["message"] = data["message"]
    if "eventCategories" in data:
        import aws_sdk_lightsail.types.string_list

        out["event_categories"] = (
            aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["eventCategories"]
            )
        )
    return out
