"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.domain_resource_filter_list


class ObjectiveFilter(TypedDict):
    domains: NotRequired[
        "aws_sdk_controlcatalog.types.domain_resource_filter_list.DomainResourceFilterList"
    ]
    """<p>The domain that's used as filter criteria.</p> <p>You can use this parameter to specify one domain ARN at a time. Passing multiple ARNs in the <code>ObjectiveFilter</code> isn’t supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveFilter) -> dict:
    out: dict = {}
    if "domains" in value:
        import aws_sdk_controlcatalog.types.domain_resource_filter_list

        out["Domains"] = (
            aws_sdk_controlcatalog.types.domain_resource_filter_list.serialize_json(
                value["domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectiveFilter:
    out: ObjectiveFilter = {}  # type: ignore[typeddict-item]
    if "Domains" in data:
        import aws_sdk_controlcatalog.types.domain_resource_filter_list

        out["domains"] = (
            aws_sdk_controlcatalog.types.domain_resource_filter_list.deserialize_json(
                data["Domains"]
            )
        )
    return out
