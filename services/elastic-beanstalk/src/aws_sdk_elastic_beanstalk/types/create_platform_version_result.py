"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreatePlatformVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.builder
    import aws_sdk_elastic_beanstalk.types.platform_summary


class CreatePlatformVersionResult(TypedDict, closed=True):
    platform_summary: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_summary.PlatformSummary"
    ]
    """<p>Detailed information about the new version of the custom platform.</p>"""
    builder: NotRequired["aws_sdk_elastic_beanstalk.types.builder.Builder"]
    """<p>The builder used to create the custom platform.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePlatformVersionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_summary" in value:
        import aws_sdk_elastic_beanstalk.types.platform_summary

        aws_sdk_elastic_beanstalk.types.platform_summary.serialize_query(
            value["platform_summary"], pairs, f"{prefix}.PlatformSummary"
        )
    if "builder" in value:
        import aws_sdk_elastic_beanstalk.types.builder

        aws_sdk_elastic_beanstalk.types.builder.serialize_query(
            value["builder"], pairs, f"{prefix}.Builder"
        )


def deserialize_query(el: Element) -> CreatePlatformVersionResult:
    out: CreatePlatformVersionResult = {}  # type: ignore[typeddict-item]
    child_platform_summary = el.find("PlatformSummary")
    if child_platform_summary is not None:
        import aws_sdk_elastic_beanstalk.types.platform_summary

        out["platform_summary"] = (
            aws_sdk_elastic_beanstalk.types.platform_summary.deserialize_query(
                child_platform_summary
            )
        )
    child_builder = el.find("Builder")
    if child_builder is not None:
        import aws_sdk_elastic_beanstalk.types.builder

        out["builder"] = aws_sdk_elastic_beanstalk.types.builder.deserialize_query(
            child_builder
        )
    return out
