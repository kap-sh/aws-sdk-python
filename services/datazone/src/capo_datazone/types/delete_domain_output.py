"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_status


class DeleteDomainOutput(TypedDict, closed=True):
    status: "capo_datazone.types.domain_status.DomainStatus"
    """<p>The status of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.domain_status

    out["status"] = capo_datazone.types.domain_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteDomainOutput:
    out: DeleteDomainOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_datazone.types.domain_status

        out["status"] = capo_datazone.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteDomainOutput.status required")
    return out
