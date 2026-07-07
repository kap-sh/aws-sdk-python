"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CancelDomainConfigChangeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cancelled_change_property_list
    import aws_sdk_elasticsearch_service.types.dry_run
    import aws_sdk_elasticsearch_service.types.guid_list


class CancelDomainConfigChangeResponse(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_elasticsearch_service.types.dry_run.DryRun"]
    """<p>Whether or not the request was a dry run. If <b>True</b>, the changes were not actually cancelled.</p>"""
    cancelled_change_ids: NotRequired[
        "aws_sdk_elasticsearch_service.types.guid_list.GUIDList"
    ]
    """<p>The unique identifiers of the changes that were cancelled.</p>"""
    cancelled_change_properties: NotRequired[
        "aws_sdk_elasticsearch_service.types.cancelled_change_property_list.CancelledChangePropertyList"
    ]
    """<p>The domain change properties that were cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelDomainConfigChangeResponse) -> dict:
    out: dict = {}
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "cancelled_change_ids" in value:
        import aws_sdk_elasticsearch_service.types.guid_list

        out["CancelledChangeIds"] = (
            aws_sdk_elasticsearch_service.types.guid_list.serialize_json(
                value["cancelled_change_ids"]
            )
        )
    if "cancelled_change_properties" in value:
        import aws_sdk_elasticsearch_service.types.cancelled_change_property_list

        out["CancelledChangeProperties"] = (
            aws_sdk_elasticsearch_service.types.cancelled_change_property_list.serialize_json(
                value["cancelled_change_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CancelDomainConfigChangeResponse:
    out: CancelDomainConfigChangeResponse = {}  # type: ignore[typeddict-item]
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    if "CancelledChangeIds" in data:
        import aws_sdk_elasticsearch_service.types.guid_list

        out["cancelled_change_ids"] = (
            aws_sdk_elasticsearch_service.types.guid_list.deserialize_json(
                data["CancelledChangeIds"]
            )
        )
    if "CancelledChangeProperties" in data:
        import aws_sdk_elasticsearch_service.types.cancelled_change_property_list

        out["cancelled_change_properties"] = (
            aws_sdk_elasticsearch_service.types.cancelled_change_property_list.deserialize_json(
                data["CancelledChangeProperties"]
            )
        )
    return out
