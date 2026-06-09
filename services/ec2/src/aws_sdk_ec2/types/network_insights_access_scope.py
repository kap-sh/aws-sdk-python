"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.tag_list


class NetworkInsightsAccessScope(TypedDict):
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    network_insights_access_scope_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Network Access Scope.</p>"""
    created_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The creation date.</p>"""
    updated_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last updated date.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAccessScope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "network_insights_access_scope_arn" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeArn",
                str(value["network_insights_access_scope_arn"]),
            )
        )
    if "created_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["created_date"], pairs, f"{prefix}.CreatedDate"
        )
    if "updated_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["updated_date"], pairs, f"{prefix}.UpdatedDate"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsAccessScope:
    out: NetworkInsightsAccessScope = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_id = el.find("NetworkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_network_insights_access_scope_arn = el.find("NetworkInsightsAccessScopeArn")
    if child_network_insights_access_scope_arn is not None:
        out["network_insights_access_scope_arn"] = str(
            child_network_insights_access_scope_arn.text or ""
        )
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["created_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_created_date
            )
        )
    child_updated_date = el.find("UpdatedDate")
    if child_updated_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["updated_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_updated_date
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
