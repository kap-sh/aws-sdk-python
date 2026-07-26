"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceErrorsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.resource_error_list


class ResourceErrorsDetails(TypedDict, closed=True):
    resource_errors: NotRequired[
        "capo_resiliencehub.types.resource_error_list.ResourceErrorList"
    ]
    """<p> A list of errors retrieving an application's resources. </p>"""
    has_more_errors: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p> This indicates if there are more errors not listed in the <code>resourceErrors</code> list. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceErrorsDetails) -> dict:
    out: dict = {}
    if "resource_errors" in value:
        import capo_resiliencehub.types.resource_error_list

        out["resourceErrors"] = (
            capo_resiliencehub.types.resource_error_list.serialize_json(
                value["resource_errors"]
            )
        )
    if "has_more_errors" in value:
        out["hasMoreErrors"] = value["has_more_errors"]
    return out


def deserialize_json(data: dict) -> ResourceErrorsDetails:
    out: ResourceErrorsDetails = {}  # type: ignore[typeddict-item]
    if "resourceErrors" in data:
        import capo_resiliencehub.types.resource_error_list

        out["resource_errors"] = (
            capo_resiliencehub.types.resource_error_list.deserialize_json(
                data["resourceErrors"]
            )
        )
    if "hasMoreErrors" in data:
        out["has_more_errors"] = data["hasMoreErrors"]
    return out
