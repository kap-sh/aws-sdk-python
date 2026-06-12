"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListIntegrationItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_names
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.object_type_names
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.role_arn
    import aws_sdk_customer_profiles.types.scope
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name


class ListIntegrationItem(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    uri: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The URI of the S3 bucket or any other type of data source.</p>"""
    object_type_name: NotRequired["aws_sdk_customer_profiles.types.type_name.typeName"]
    """<p>The name of the profile object type.</p>"""
    created_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the domain was created.</p>"""
    last_updated_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the integration was most recently edited.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    object_type_names: NotRequired[
        "aws_sdk_customer_profiles.types.object_type_names.ObjectTypeNames"
    ]
    """<p>A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an <code>ObjectTypeName</code> (template) used to ingest the event. It supports the following event types: <code>SegmentIdentify</code>, <code>ShopifyCreateCustomers</code>, <code>ShopifyUpdateCustomers</code>, <code>ShopifyCreateDraftOrders</code>, <code>ShopifyUpdateDraftOrders</code>, <code>ShopifyCreateOrders</code>, and <code>ShopifyUpdatedOrders</code>.</p>"""
    workflow_id: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>Unique identifier for the workflow.</p>"""
    is_unstructured: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Boolean that shows if the Flow that's associated with the Integration is created in Amazon Appflow, or with ObjectTypeName equals _unstructured via API/CLI in flowDefinition.</p>"""
    role_arn: NotRequired["aws_sdk_customer_profiles.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.</p>"""
    event_trigger_names: NotRequired[
        "aws_sdk_customer_profiles.types.event_trigger_names.EventTriggerNames"
    ]
    """<p>A list of unique names for active event triggers associated with the integration.</p>"""
    scope: NotRequired["aws_sdk_customer_profiles.types.scope.Scope"]
    """<p>The scope or boundary of the integration item's applicability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegrationItem) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["Uri"] = value["uri"]
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    import aws_sdk_customer_profiles.types.timestamp

    out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    if "object_type_names" in value:
        import aws_sdk_customer_profiles.types.object_type_names

        out["ObjectTypeNames"] = (
            aws_sdk_customer_profiles.types.object_type_names.serialize_json(
                value["object_type_names"]
            )
        )
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "is_unstructured" in value:
        out["IsUnstructured"] = value["is_unstructured"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "event_trigger_names" in value:
        import aws_sdk_customer_profiles.types.event_trigger_names

        out["EventTriggerNames"] = (
            aws_sdk_customer_profiles.types.event_trigger_names.serialize_json(
                value["event_trigger_names"]
            )
        )
    if "scope" in value:
        import aws_sdk_customer_profiles.types.scope

        out["Scope"] = aws_sdk_customer_profiles.types.scope.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> ListIntegrationItem:
    out: ListIntegrationItem = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("ListIntegrationItem.domain_name required")
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("ListIntegrationItem.uri required")
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("ListIntegrationItem.created_at required")
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("ListIntegrationItem.last_updated_at required")
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "ObjectTypeNames" in data:
        import aws_sdk_customer_profiles.types.object_type_names

        out["object_type_names"] = (
            aws_sdk_customer_profiles.types.object_type_names.deserialize_json(
                data["ObjectTypeNames"]
            )
        )
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    if "IsUnstructured" in data:
        out["is_unstructured"] = data["IsUnstructured"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "EventTriggerNames" in data:
        import aws_sdk_customer_profiles.types.event_trigger_names

        out["event_trigger_names"] = (
            aws_sdk_customer_profiles.types.event_trigger_names.deserialize_json(
                data["EventTriggerNames"]
            )
        )
    if "Scope" in data:
        import aws_sdk_customer_profiles.types.scope

        out["scope"] = aws_sdk_customer_profiles.types.scope.deserialize_json(
            data["Scope"]
        )
    return out
