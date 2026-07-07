"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeDefaultClusterParametersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.default_cluster_parameters


class DescribeDefaultClusterParametersResult(TypedDict, closed=True):
    default_cluster_parameters: NotRequired[
        "aws_sdk_redshift.types.default_cluster_parameters.DefaultClusterParameters"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDefaultClusterParametersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "default_cluster_parameters" in value:
        import aws_sdk_redshift.types.default_cluster_parameters

        aws_sdk_redshift.types.default_cluster_parameters.serialize_query(
            value["default_cluster_parameters"],
            pairs,
            f"{prefix}.DefaultClusterParameters",
        )


def deserialize_query(el: Element) -> DescribeDefaultClusterParametersResult:
    out: DescribeDefaultClusterParametersResult = {}  # type: ignore[typeddict-item]
    child_default_cluster_parameters = el.find("DefaultClusterParameters")
    if child_default_cluster_parameters is not None:
        import aws_sdk_redshift.types.default_cluster_parameters

        out["default_cluster_parameters"] = (
            aws_sdk_redshift.types.default_cluster_parameters.deserialize_query(
                child_default_cluster_parameters
            )
        )
    return out
