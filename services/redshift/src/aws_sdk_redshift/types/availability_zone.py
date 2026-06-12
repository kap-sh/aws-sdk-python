"""Generated from Smithy shape ``com.amazonaws.redshift#AvailabilityZone``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.supported_platforms_list


class AvailabilityZone(TypedDict):
    name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the availability zone.</p>"""
    supported_platforms: NotRequired[
        "aws_sdk_redshift.types.supported_platforms_list.SupportedPlatformsList"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZone, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "supported_platforms" in value:
        import aws_sdk_redshift.types.supported_platforms_list

        aws_sdk_redshift.types.supported_platforms_list.serialize_query(
            value["supported_platforms"], pairs, f"{prefix}.SupportedPlatforms"
        )


def deserialize_query(el: Element) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_supported_platforms = el.find("SupportedPlatforms")
    if child_supported_platforms is not None:
        import aws_sdk_redshift.types.supported_platforms_list

        out["supported_platforms"] = (
            aws_sdk_redshift.types.supported_platforms_list.deserialize_query(
                child_supported_platforms
            )
        )
    return out
