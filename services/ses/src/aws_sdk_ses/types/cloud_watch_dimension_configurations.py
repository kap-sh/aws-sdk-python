"""Generated from Smithy shape ``com.amazonaws.ses#CloudWatchDimensionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.cloud_watch_dimension_configuration

CloudWatchDimensionConfigurations: TypeAlias = list[
    "aws_sdk_ses.types.cloud_watch_dimension_configuration.CloudWatchDimensionConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudWatchDimensionConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.cloud_watch_dimension_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.cloud_watch_dimension_configuration.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CloudWatchDimensionConfigurations:
    import aws_sdk_ses.types.cloud_watch_dimension_configuration

    out: CloudWatchDimensionConfigurations = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_ses.types.cloud_watch_dimension_configuration.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: CloudWatchDimensionConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.cloud_watch_dimension_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.cloud_watch_dimension_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> CloudWatchDimensionConfigurations:
    import aws_sdk_ses.types.cloud_watch_dimension_configuration

    out: CloudWatchDimensionConfigurations = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ses.types.cloud_watch_dimension_configuration.deserialize_query(
                child
            )
        )
    return out
