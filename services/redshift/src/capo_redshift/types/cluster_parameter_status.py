"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class ClusterParameterStatus(TypedDict, closed=True):
    parameter_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the parameter.</p>"""
    parameter_apply_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.</p> <p>The following are possible statuses and descriptions.</p> <ul> <li> <p> <code>in-sync</code>: The parameter value is in sync with the database.</p> </li> <li> <p> <code>pending-reboot</code>: The parameter value will be applied after the cluster reboots.</p> </li> <li> <p> <code>applying</code>: The parameter value is being applied to the database.</p> </li> <li> <p> <code>invalid-parameter</code>: Cannot apply the parameter value because it has an invalid value or syntax.</p> </li> <li> <p> <code>apply-deferred</code>: The parameter contains static property changes. The changes are deferred until the cluster reboots.</p> </li> <li> <p> <code>apply-error</code>: Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.</p> </li> <li> <p> <code>unknown-error</code>: Cannot apply the parameter change right now. The change will be applied after the cluster reboots.</p> </li> </ul>"""
    parameter_apply_error_description: NotRequired["capo_redshift.types.string.String"]
    """<p>The error that prevented the parameter from being applied to the database.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_name" in value:
        pairs.append((f"{key_prefix}ParameterName", str(value["parameter_name"])))
    if "parameter_apply_status" in value:
        pairs.append(
            (f"{key_prefix}ParameterApplyStatus", str(value["parameter_apply_status"]))
        )
    if "parameter_apply_error_description" in value:
        pairs.append(
            (
                f"{key_prefix}ParameterApplyErrorDescription",
                str(value["parameter_apply_error_description"]),
            )
        )


def deserialize_query(el: Element) -> ClusterParameterStatus:
    out: ClusterParameterStatus = {}  # type: ignore[typeddict-item]
    child_parameter_name = el.find("ParameterName")
    if child_parameter_name is not None:
        out["parameter_name"] = str(child_parameter_name.text or "")
    child_parameter_apply_status = el.find("ParameterApplyStatus")
    if child_parameter_apply_status is not None:
        out["parameter_apply_status"] = str(child_parameter_apply_status.text or "")
    child_parameter_apply_error_description = el.find("ParameterApplyErrorDescription")
    if child_parameter_apply_error_description is not None:
        out["parameter_apply_error_description"] = str(
            child_parameter_apply_error_description.text or ""
        )
    return out
