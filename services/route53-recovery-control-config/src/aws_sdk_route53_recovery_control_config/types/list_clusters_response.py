"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__list_of_cluster
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max8096_pattern_s


class ListClustersResponse(TypedDict, closed=True):
    clusters: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__list_of_cluster.__listOfCluster"
    ]
    """<p>An array of the clusters in an account.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max8096_pattern_s.__stringMin1Max8096PatternS"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "clusters" in value:
        import aws_sdk_route53_recovery_control_config.types.__list_of_cluster

        out["Clusters"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of_cluster.serialize_json(
                value["clusters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "Clusters" in data:
        import aws_sdk_route53_recovery_control_config.types.__list_of_cluster

        out["clusters"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of_cluster.deserialize_json(
                data["Clusters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
