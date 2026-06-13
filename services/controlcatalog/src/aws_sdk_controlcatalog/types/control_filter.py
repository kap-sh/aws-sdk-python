"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.governed_provider_filter_list
    import aws_sdk_controlcatalog.types.implementation_filter


class ControlFilter(TypedDict):
    implementations: NotRequired[
        "aws_sdk_controlcatalog.types.implementation_filter.ImplementationFilter"
    ]
    """<p>A filter that narrows the results to controls with specific implementation types or identifiers. This field allows you to find controls that are implemented by specific Amazon Web Services services or with specific service identifiers.</p>"""
    governed_providers: NotRequired[
        "aws_sdk_controlcatalog.types.governed_provider_filter_list.GovernedProviderFilterList"
    ]
    """<p>A filter that narrows the results to controls that govern a specific provider's resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlFilter) -> dict:
    out: dict = {}
    if "implementations" in value:
        import aws_sdk_controlcatalog.types.implementation_filter

        out["Implementations"] = (
            aws_sdk_controlcatalog.types.implementation_filter.serialize_json(
                value["implementations"]
            )
        )
    if "governed_providers" in value:
        import aws_sdk_controlcatalog.types.governed_provider_filter_list

        out["GovernedProviders"] = (
            aws_sdk_controlcatalog.types.governed_provider_filter_list.serialize_json(
                value["governed_providers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlFilter:
    out: ControlFilter = {}  # type: ignore[typeddict-item]
    if "Implementations" in data:
        import aws_sdk_controlcatalog.types.implementation_filter

        out["implementations"] = (
            aws_sdk_controlcatalog.types.implementation_filter.deserialize_json(
                data["Implementations"]
            )
        )
    if "GovernedProviders" in data:
        import aws_sdk_controlcatalog.types.governed_provider_filter_list

        out["governed_providers"] = (
            aws_sdk_controlcatalog.types.governed_provider_filter_list.deserialize_json(
                data["GovernedProviders"]
            )
        )
    return out
