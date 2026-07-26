"""Generated from Smithy shape ``com.amazonaws.sns#PlatformApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.map_string_to_string
    import capo_sns.types.string


class PlatformApplication(TypedDict, closed=True):
    platform_application_arn: NotRequired["capo_sns.types.string.String"]
    """<p>PlatformApplicationArn for platform application object.</p>"""
    attributes: NotRequired["capo_sns.types.map_string_to_string.MapStringToString"]
    """<p>Attributes for platform application object.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformApplication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_application_arn" in value:
        pairs.append(
            (f"{prefix}.PlatformApplicationArn", str(value["platform_application_arn"]))
        )
    if "attributes" in value:
        import capo_sns.types.map_string_to_string

        capo_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> PlatformApplication:
    out: PlatformApplication = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.map_string_to_string

        out["attributes"] = capo_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
