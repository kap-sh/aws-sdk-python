"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.verified_access_sse_specification_response


class VerifiedAccessGroup(TypedDict, closed=True):
    verified_access_group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Verified Access group.</p>"""
    verified_access_instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access group.</p>"""
    owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account number that owns the group.</p>"""
    verified_access_group_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Verified Access group.</p>"""
    creation_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    deletion_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The deletion time.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    sse_specification: NotRequired[
        "capo_ec2.types.verified_access_sse_specification_response.VerifiedAccessSseSpecificationResponse"
    ]
    """<p>The options in use for server side encryption.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessGroupId",
                str(value["verified_access_group_id"]),
            )
        )
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "owner" in value:
        pairs.append((f"{key_prefix}Owner", str(value["owner"])))
    if "verified_access_group_arn" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessGroupArn",
                str(value["verified_access_group_arn"]),
            )
        )
    if "creation_time" in value:
        pairs.append((f"{key_prefix}CreationTime", str(value["creation_time"])))
    if "last_updated_time" in value:
        pairs.append((f"{key_prefix}LastUpdatedTime", str(value["last_updated_time"])))
    if "deletion_time" in value:
        pairs.append((f"{key_prefix}DeletionTime", str(value["deletion_time"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "sse_specification" in value:
        import capo_ec2.types.verified_access_sse_specification_response

        capo_ec2.types.verified_access_sse_specification_response.serialize_ec2_query(
            value["sse_specification"], pairs, f"{key_prefix}SseSpecification"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessGroup:
    out: VerifiedAccessGroup = {}  # type: ignore[typeddict-item]
    child_verified_access_group_id = el.find("VerifiedAccessGroupId")
    if child_verified_access_group_id is not None:
        out["verified_access_group_id"] = str(child_verified_access_group_id.text or "")
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_owner = el.find("Owner")
    if child_owner is not None:
        out["owner"] = str(child_owner.text or "")
    child_verified_access_group_arn = el.find("VerifiedAccessGroupArn")
    if child_verified_access_group_arn is not None:
        out["verified_access_group_arn"] = str(
            child_verified_access_group_arn.text or ""
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        out["creation_time"] = str(child_creation_time.text or "")
    child_last_updated_time = el.find("LastUpdatedTime")
    if child_last_updated_time is not None:
        out["last_updated_time"] = str(child_last_updated_time.text or "")
    child_deletion_time = el.find("DeletionTime")
    if child_deletion_time is not None:
        out["deletion_time"] = str(child_deletion_time.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import capo_ec2.types.verified_access_sse_specification_response

        out["sse_specification"] = (
            capo_ec2.types.verified_access_sse_specification_response.deserialize_ec2_query(
                child_sse_specification
            )
        )
    return out
