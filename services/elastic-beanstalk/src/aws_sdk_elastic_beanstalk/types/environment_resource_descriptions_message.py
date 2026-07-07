"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentResourceDescriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_resource_description


class EnvironmentResourceDescriptionsMessage(TypedDict, closed=True):
    environment_resources: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_resource_description.EnvironmentResourceDescription"
    ]
    """<p> A list of <a>EnvironmentResourceDescription</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentResourceDescriptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "environment_resources" in value:
        import aws_sdk_elastic_beanstalk.types.environment_resource_description

        aws_sdk_elastic_beanstalk.types.environment_resource_description.serialize_query(
            value["environment_resources"], pairs, f"{prefix}.EnvironmentResources"
        )


def deserialize_query(el: Element) -> EnvironmentResourceDescriptionsMessage:
    out: EnvironmentResourceDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_environment_resources = el.find("EnvironmentResources")
    if child_environment_resources is not None:
        import aws_sdk_elastic_beanstalk.types.environment_resource_description

        out["environment_resources"] = (
            aws_sdk_elastic_beanstalk.types.environment_resource_description.deserialize_query(
                child_environment_resources
            )
        )
    return out
