"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CloudComponentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.cloud_component_state
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.string_map
    import capo_greengrassv2.types.vendor_guidance


class CloudComponentStatus(TypedDict, closed=True):
    component_state: NotRequired[
        "capo_greengrassv2.types.cloud_component_state.CloudComponentState"
    ]
    """<p>The state of the component version.</p>"""
    message: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>A message that communicates details, such as errors, about the status of the component version.</p>"""
    errors: NotRequired["capo_greengrassv2.types.string_map.StringMap"]
    """<p>A dictionary of errors that communicate why the component version is in an error state. For example, if IoT Greengrass can't access an artifact for the component version, then <code>errors</code> contains the artifact's URI as a key, and the error message as the value for that key.</p>"""
    vendor_guidance: NotRequired[
        "capo_greengrassv2.types.vendor_guidance.VendorGuidance"
    ]
    """<p>The vendor guidance state for the component version. This state indicates whether the component version has any issues that you should consider before you deploy it. The vendor guidance state can be:</p> <ul> <li> <p> <code>ACTIVE</code> – This component version is available and recommended for use.</p> </li> <li> <p> <code>DISCONTINUED</code> – This component version has been discontinued by its publisher. You can deploy this component version, but we recommend that you use a different version of this component.</p> </li> <li> <p> <code>DELETED</code> – This component version has been deleted by its publisher, so you can't deploy it. If you have any existing deployments that specify this component version, those deployments will fail.</p> </li> </ul>"""
    vendor_guidance_message: NotRequired[
        "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A message that communicates details about the vendor guidance state of the component version. This message communicates why a component version is discontinued or deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudComponentStatus) -> dict:
    out: dict = {}
    if "component_state" in value:
        import capo_greengrassv2.types.cloud_component_state

        out["componentState"] = (
            capo_greengrassv2.types.cloud_component_state.serialize_json(
                value["component_state"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "errors" in value:
        import capo_greengrassv2.types.string_map

        out["errors"] = capo_greengrassv2.types.string_map.serialize_json(
            value["errors"]
        )
    if "vendor_guidance" in value:
        import capo_greengrassv2.types.vendor_guidance

        out["vendorGuidance"] = capo_greengrassv2.types.vendor_guidance.serialize_json(
            value["vendor_guidance"]
        )
    if "vendor_guidance_message" in value:
        out["vendorGuidanceMessage"] = value["vendor_guidance_message"]
    return out


def deserialize_json(data: dict) -> CloudComponentStatus:
    out: CloudComponentStatus = {}  # type: ignore[typeddict-item]
    if "componentState" in data:
        import capo_greengrassv2.types.cloud_component_state

        out["component_state"] = (
            capo_greengrassv2.types.cloud_component_state.deserialize_json(
                data["componentState"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "errors" in data:
        import capo_greengrassv2.types.string_map

        out["errors"] = capo_greengrassv2.types.string_map.deserialize_json(
            data["errors"]
        )
    if "vendorGuidance" in data:
        import capo_greengrassv2.types.vendor_guidance

        out["vendor_guidance"] = (
            capo_greengrassv2.types.vendor_guidance.deserialize_json(
                data["vendorGuidance"]
            )
        )
    if "vendorGuidanceMessage" in data:
        out["vendor_guidance_message"] = data["vendorGuidanceMessage"]
    return out
