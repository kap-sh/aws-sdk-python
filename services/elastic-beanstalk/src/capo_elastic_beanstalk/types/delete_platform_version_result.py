"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeletePlatformVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_summary


class DeletePlatformVersionResult(TypedDict, closed=True):
    platform_summary: NotRequired[
        "capo_elastic_beanstalk.types.platform_summary.PlatformSummary"
    ]
    """<p>Detailed information about the version of the custom platform.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePlatformVersionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_summary" in value:
        import capo_elastic_beanstalk.types.platform_summary

        capo_elastic_beanstalk.types.platform_summary.serialize_query(
            value["platform_summary"], pairs, f"{prefix}.PlatformSummary"
        )


def deserialize_query(el: Element) -> DeletePlatformVersionResult:
    out: DeletePlatformVersionResult = {}  # type: ignore[typeddict-item]
    child_platform_summary = el.find("PlatformSummary")
    if child_platform_summary is not None:
        import capo_elastic_beanstalk.types.platform_summary

        out["platform_summary"] = (
            capo_elastic_beanstalk.types.platform_summary.deserialize_query(
                child_platform_summary
            )
        )
    return out
