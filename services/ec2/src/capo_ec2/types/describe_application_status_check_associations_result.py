"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeApplicationStatusCheckAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_association_set
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class DescribeApplicationStatusCheckAssociationsResult(TypedDict, closed=True):
    associations: NotRequired[
        "capo_ec2.types.application_status_check_association_set.ApplicationStatusCheckAssociationSet"
    ]
    """<p>The associations for the specified application status checks.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the application status checks.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeApplicationStatusCheckAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "associations" in value:
        import capo_ec2.types.application_status_check_association_set

        capo_ec2.types.application_status_check_association_set.serialize_ec2_query(
            value["associations"], pairs, f"{key_prefix}AssociationSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeApplicationStatusCheckAssociationsResult:
    out: DescribeApplicationStatusCheckAssociationsResult = {}  # type: ignore[typeddict-item]
    child_associations = el.find("associationSet")
    if child_associations is not None:
        import capo_ec2.types.application_status_check_association_set

        out["associations"] = (
            capo_ec2.types.application_status_check_association_set.deserialize_ec2_query(
                child_associations
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
