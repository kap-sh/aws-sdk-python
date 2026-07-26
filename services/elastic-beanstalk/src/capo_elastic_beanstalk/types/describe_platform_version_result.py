"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribePlatformVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_description


class DescribePlatformVersionResult(TypedDict, closed=True):
    platform_description: NotRequired[
        "capo_elastic_beanstalk.types.platform_description.PlatformDescription"
    ]
    """<p>Detailed information about the platform version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePlatformVersionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_description" in value:
        import capo_elastic_beanstalk.types.platform_description

        capo_elastic_beanstalk.types.platform_description.serialize_query(
            value["platform_description"], pairs, f"{prefix}.PlatformDescription"
        )


def deserialize_query(el: Element) -> DescribePlatformVersionResult:
    out: DescribePlatformVersionResult = {}  # type: ignore[typeddict-item]
    child_platform_description = el.find("PlatformDescription")
    if child_platform_description is not None:
        import capo_elastic_beanstalk.types.platform_description

        out["platform_description"] = (
            capo_elastic_beanstalk.types.platform_description.deserialize_query(
                child_platform_description
            )
        )
    return out
