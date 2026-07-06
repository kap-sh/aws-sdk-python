"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.replication_destination_list
    import aws_sdk_ecr.types.repository_filter_list


class ReplicationRule(TypedDict, closed=True):
    destinations: (
        "aws_sdk_ecr.types.replication_destination_list.ReplicationDestinationList"
    )
    """<p>An array of objects representing the destination for a replication rule.</p>"""
    repository_filters: NotRequired[
        "aws_sdk_ecr.types.repository_filter_list.RepositoryFilterList"
    ]
    """<p>An array of objects representing the filters for a replication rule. Specifying a repository filter for a replication rule provides a method for controlling which repositories in a private registry are replicated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationRule) -> dict:
    out: dict = {}
    import aws_sdk_ecr.types.replication_destination_list

    out["destinations"] = (
        aws_sdk_ecr.types.replication_destination_list.serialize_aws_json_1_1(
            value["destinations"]
        )
    )
    if "repository_filters" in value:
        import aws_sdk_ecr.types.repository_filter_list

        out["repositoryFilters"] = (
            aws_sdk_ecr.types.repository_filter_list.serialize_aws_json_1_1(
                value["repository_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationRule:
    out: ReplicationRule = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_ecr.types.replication_destination_list

        out["destinations"] = (
            aws_sdk_ecr.types.replication_destination_list.deserialize_aws_json_1_1(
                data["destinations"]
            )
        )
    else:
        raise DeserializationError("ReplicationRule.destinations required")
    if "repositoryFilters" in data:
        import aws_sdk_ecr.types.repository_filter_list

        out["repository_filters"] = (
            aws_sdk_ecr.types.repository_filter_list.deserialize_aws_json_1_1(
                data["repositoryFilters"]
            )
        )
    return out
