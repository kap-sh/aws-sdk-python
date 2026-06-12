"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeletePlatformVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.platform_summary


class DeletePlatformVersionResult(TypedDict):
    platform_summary: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_summary.PlatformSummary"
    ]
    """<p>Detailed information about the version of the custom platform.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePlatformVersionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_summary" in value:
        import aws_sdk_elastic_beanstalk.types.platform_summary

        aws_sdk_elastic_beanstalk.types.platform_summary.serialize_query(
            value["platform_summary"], pairs, f"{prefix}.PlatformSummary"
        )


def deserialize_query(el: Element) -> DeletePlatformVersionResult:
    out: DeletePlatformVersionResult = {}  # type: ignore[typeddict-item]
    child_platform_summary = el.find("PlatformSummary")
    if child_platform_summary is not None:
        import aws_sdk_elastic_beanstalk.types.platform_summary

        out["platform_summary"] = (
            aws_sdk_elastic_beanstalk.types.platform_summary.deserialize_query(
                child_platform_summary
            )
        )
    return out
