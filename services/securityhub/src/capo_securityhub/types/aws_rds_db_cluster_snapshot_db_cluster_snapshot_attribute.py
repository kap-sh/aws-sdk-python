"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute(TypedDict, closed=True):
    attribute_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the manual DB cluster snapshot attribute. The attribute named <code>restore</code> refers to the list of Amazon Web Services accounts that have permission to copy or restore the manual DB cluster snapshot. </p>"""
    attribute_values: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The value(s) for the manual DB cluster snapshot attribute. If the <code>AttributeName</code> field is set to <code>restore</code>, then this element returns a list of IDs of the Amazon Web Services accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of <code>all</code> is in the list, then the manual DB cluster snapshot is public and available for any Amazon Web Services account to copy or restore. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "attribute_values" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AttributeValues"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["attribute_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute:
    out: AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "AttributeValues" in data:
        import capo_securityhub.types.non_empty_string_list

        out["attribute_values"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AttributeValues"]
            )
        )
    return out
