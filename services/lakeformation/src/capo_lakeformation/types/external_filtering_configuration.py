"""Generated from Smithy shape ``com.amazonaws.lakeformation#ExternalFilteringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.enable_status
    import capo_lakeformation.types.scope_targets


class ExternalFilteringConfiguration(TypedDict, closed=True):
    status: "capo_lakeformation.types.enable_status.EnableStatus"
    """<p>Allows to enable or disable the third-party applications that are allowed to access data managed by Lake Formation.</p>"""
    authorized_targets: "capo_lakeformation.types.scope_targets.ScopeTargets"
    """<p>List of third-party application <code>ARNs</code> integrated with Lake Formation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalFilteringConfiguration) -> dict:
    out: dict = {}
    import capo_lakeformation.types.enable_status

    out["Status"] = capo_lakeformation.types.enable_status.serialize_json(
        value["status"]
    )
    import capo_lakeformation.types.scope_targets

    out["AuthorizedTargets"] = capo_lakeformation.types.scope_targets.serialize_json(
        value["authorized_targets"]
    )
    return out


def deserialize_json(data: dict) -> ExternalFilteringConfiguration:
    out: ExternalFilteringConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_lakeformation.types.enable_status

        out["status"] = capo_lakeformation.types.enable_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("ExternalFilteringConfiguration.status required")
    if "AuthorizedTargets" in data:
        import capo_lakeformation.types.scope_targets

        out["authorized_targets"] = (
            capo_lakeformation.types.scope_targets.deserialize_json(
                data["AuthorizedTargets"]
            )
        )
    else:
        raise DeserializationError(
            "ExternalFilteringConfiguration.authorized_targets required"
        )
    return out
