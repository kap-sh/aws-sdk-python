"""Generated from Smithy shape ``com.amazonaws.opensearch#EBSOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.ebs_options
    import capo_opensearch.types.option_status


class EBSOptionsStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.ebs_options.EBSOptions"
    """<p>The configured EBS options for the specified domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of the EBS options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSOptionsStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.ebs_options

    out["Options"] = capo_opensearch.types.ebs_options.serialize_json(value["options"])
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> EBSOptionsStatus:
    out: EBSOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.ebs_options

        out["options"] = capo_opensearch.types.ebs_options.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("EBSOptionsStatus.options required")
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("EBSOptionsStatus.status required")
    return out
