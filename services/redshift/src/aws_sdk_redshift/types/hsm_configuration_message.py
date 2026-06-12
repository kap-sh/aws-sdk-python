"""Generated from Smithy shape ``com.amazonaws.redshift#HsmConfigurationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.hsm_configuration_list
    import aws_sdk_redshift.types.string


class HsmConfigurationMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    hsm_configurations: NotRequired[
        "aws_sdk_redshift.types.hsm_configuration_list.HsmConfigurationList"
    ]
    """<p>A list of <code>HsmConfiguration</code> objects.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmConfigurationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "hsm_configurations" in value:
        import aws_sdk_redshift.types.hsm_configuration_list

        aws_sdk_redshift.types.hsm_configuration_list.serialize_query(
            value["hsm_configurations"], pairs, f"{prefix}.HsmConfigurations"
        )


def deserialize_query(el: Element) -> HsmConfigurationMessage:
    out: HsmConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_hsm_configurations = el.find("HsmConfigurations")
    if child_hsm_configurations is not None:
        import aws_sdk_redshift.types.hsm_configuration_list

        out["hsm_configurations"] = (
            aws_sdk_redshift.types.hsm_configuration_list.deserialize_query(
                child_hsm_configurations
            )
        )
    return out
