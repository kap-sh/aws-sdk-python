"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribePlatformVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.platform_description


class DescribePlatformVersionResult(TypedDict):
    platform_description: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_description.PlatformDescription"
    ]
    """<p>Detailed information about the platform version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePlatformVersionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_description" in value:
        import aws_sdk_elastic_beanstalk.types.platform_description

        aws_sdk_elastic_beanstalk.types.platform_description.serialize_query(
            value["platform_description"], pairs, f"{prefix}.PlatformDescription"
        )


def deserialize_query(el: Element) -> DescribePlatformVersionResult:
    out: DescribePlatformVersionResult = {}  # type: ignore[typeddict-item]
    child_platform_description = el.find("PlatformDescription")
    if child_platform_description is not None:
        import aws_sdk_elastic_beanstalk.types.platform_description

        out["platform_description"] = (
            aws_sdk_elastic_beanstalk.types.platform_description.deserialize_query(
                child_platform_description
            )
        )
    return out
