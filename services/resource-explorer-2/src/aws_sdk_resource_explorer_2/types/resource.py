"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resource_explorer_2.types.resource_property_list


class Resource(TypedDict):
    arn: NotRequired["str"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the resource.</p>"""
    owning_account_id: NotRequired["str"]
    """<p>The Amazon Web Services account that owns the resource.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region in which the resource was created and exists.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource.</p>"""
    service: NotRequired["str"]
    """<p>The Amazon Web Services service that owns the resource and is responsible for creating and updating it.</p>"""
    last_reported_at: NotRequired["datetime.datetime"]
    """<p>The date and time that Resource Explorer last queried this resource and updated the index with the latest information about the resource.</p>"""
    properties: NotRequired[
        "aws_sdk_resource_explorer_2.types.resource_property_list.ResourcePropertyList"
    ]
    """<p>A structure with additional type-specific details about the resource. These properties can be added by turning on integration between Resource Explorer and other Amazon Web Services services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owning_account_id" in value:
        out["OwningAccountId"] = value["owning_account_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "service" in value:
        out["Service"] = value["service"]
    if "last_reported_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["LastReportedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["last_reported_at"]
            )
        )
    if "properties" in value:
        import aws_sdk_resource_explorer_2.types.resource_property_list

        out["Properties"] = (
            aws_sdk_resource_explorer_2.types.resource_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OwningAccountId" in data:
        out["owning_account_id"] = data["OwningAccountId"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Service" in data:
        out["service"] = data["Service"]
    if "LastReportedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["last_reported_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["LastReportedAt"]
            )
        )
    if "Properties" in data:
        import aws_sdk_resource_explorer_2.types.resource_property_list

        out["properties"] = (
            aws_sdk_resource_explorer_2.types.resource_property_list.deserialize_json(
                data["Properties"]
            )
        )
    return out
