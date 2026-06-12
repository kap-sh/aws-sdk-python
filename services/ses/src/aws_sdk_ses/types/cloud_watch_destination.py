"""Generated from Smithy shape ``com.amazonaws.ses#CloudWatchDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.cloud_watch_dimension_configurations


class CloudWatchDestination(TypedDict):
    dimension_configurations: "aws_sdk_ses.types.cloud_watch_dimension_configurations.CloudWatchDimensionConfigurations"
    """<p>A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudWatchDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.cloud_watch_dimension_configurations

    aws_sdk_ses.types.cloud_watch_dimension_configurations.serialize_query(
        value["dimension_configurations"], pairs, f"{prefix}.DimensionConfigurations"
    )


def deserialize_query(el: Element) -> CloudWatchDestination:
    out: CloudWatchDestination = {}  # type: ignore[typeddict-item]
    child_dimension_configurations = el.find("DimensionConfigurations")
    if child_dimension_configurations is not None:
        import aws_sdk_ses.types.cloud_watch_dimension_configurations

        out["dimension_configurations"] = (
            aws_sdk_ses.types.cloud_watch_dimension_configurations.deserialize_query(
                child_dimension_configurations
            )
        )
    else:
        raise DeserializationError(
            "CloudWatchDestination.dimension_configurations required"
        )
    return out
