"""Generated from Smithy shape ``com.amazonaws.opensearch#SoftwareUpdateOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.option_status
    import capo_opensearch.types.software_update_options


class SoftwareUpdateOptionsStatus(TypedDict, closed=True):
    options: NotRequired[
        "capo_opensearch.types.software_update_options.SoftwareUpdateOptions"
    ]
    """<p>The service software update options for a domain.</p>"""
    status: NotRequired["capo_opensearch.types.option_status.OptionStatus"]
    """<p>The status of service software update options, including creation date and last updated date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareUpdateOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_opensearch.types.software_update_options

        out["Options"] = capo_opensearch.types.software_update_options.serialize_json(
            value["options"]
        )
    if "status" in value:
        import capo_opensearch.types.option_status

        out["Status"] = capo_opensearch.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> SoftwareUpdateOptionsStatus:
    out: SoftwareUpdateOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.software_update_options

        out["options"] = capo_opensearch.types.software_update_options.deserialize_json(
            data["Options"]
        )
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
