"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeregistrationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.delete_resources


class DeregistrationPolicy(TypedDict, closed=True):
    delete_resources: NotRequired[
        "capo_auditmanager.types.delete_resources.DeleteResources"
    ]
    """<p>Specifies which Audit Manager data will be deleted when you deregister Audit Manager.</p> <ul> <li> <p>If you set the value to <code>ALL</code>, all of your data is deleted within seven days of deregistration.</p> </li> <li> <p>If you set the value to <code>DEFAULT</code>, none of your data is deleted at the time of deregistration. However, keep in mind that the Audit Manager data retention policy still applies. As a result, any evidence data will be deleted two years after its creation date. Your other Audit Manager resources will continue to exist indefinitely.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregistrationPolicy) -> dict:
    out: dict = {}
    if "delete_resources" in value:
        import capo_auditmanager.types.delete_resources

        out["deleteResources"] = (
            capo_auditmanager.types.delete_resources.serialize_json(
                value["delete_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeregistrationPolicy:
    out: DeregistrationPolicy = {}  # type: ignore[typeddict-item]
    if "deleteResources" in data:
        import capo_auditmanager.types.delete_resources

        out["delete_resources"] = (
            capo_auditmanager.types.delete_resources.deserialize_json(
                data["deleteResources"]
            )
        )
    return out
