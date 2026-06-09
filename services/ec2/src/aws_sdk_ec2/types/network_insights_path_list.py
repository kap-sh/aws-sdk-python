"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsPathList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_path

NetworkInsightsPathList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_path.NetworkInsightsPath"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsPathList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.network_insights_path

        aws_sdk_ec2.types.network_insights_path.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NetworkInsightsPathList:
    import aws_sdk_ec2.types.network_insights_path

    out: NetworkInsightsPathList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.network_insights_path.deserialize_ec2_query(child))
    return out
