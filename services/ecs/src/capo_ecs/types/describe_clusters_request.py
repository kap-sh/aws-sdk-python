"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.cluster_field_list
    import capo_ecs.types.string_list


class DescribeClustersRequest(TypedDict, closed=True):
    clusters: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.</p>"""
    include: NotRequired["capo_ecs.types.cluster_field_list.ClusterFieldList"]
    """<p>Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isn't included.</p> <p>If <code>ATTACHMENTS</code> is specified, the attachments for the container instances or tasks within the cluster are included, for example the capacity providers.</p> <p>If <code>SETTINGS</code> is specified, the settings for the cluster are included.</p> <p>If <code>CONFIGURATIONS</code> is specified, the configuration for the cluster is included.</p> <p>If <code>STATISTICS</code> is specified, the task and service count is included, separated by launch type.</p> <p>If <code>TAGS</code> is specified, the metadata tags associated with the cluster are included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersRequest) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_ecs.types.string_list

        out["clusters"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["clusters"]
        )
    if "include" in value:
        import capo_ecs.types.cluster_field_list

        out["include"] = capo_ecs.types.cluster_field_list.serialize_aws_json_1_1(
            value["include"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersRequest:
    out: DescribeClustersRequest = {}  # type: ignore[typeddict-item]
    if "clusters" in data:
        import capo_ecs.types.string_list

        out["clusters"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["clusters"]
        )
    if "include" in data:
        import capo_ecs.types.cluster_field_list

        out["include"] = capo_ecs.types.cluster_field_list.deserialize_aws_json_1_1(
            data["include"]
        )
    return out
