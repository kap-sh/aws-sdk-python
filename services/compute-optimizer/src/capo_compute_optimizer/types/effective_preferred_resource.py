"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EffectivePreferredResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.preferred_resource_name
    import capo_compute_optimizer.types.preferred_resource_values


class EffectivePreferredResource(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_name.PreferredResourceName"
    ]
    """<p> The name of the preferred resource list. </p>"""
    include_list: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_values.PreferredResourceValues"
    ]
    """<p> The list of preferred resource values that you want considered as rightsizing recommendation candidates. </p>"""
    effective_include_list: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_values.PreferredResourceValues"
    ]
    """<p> The expanded version of your preferred resource's include list. </p>"""
    exclude_list: NotRequired[
        "capo_compute_optimizer.types.preferred_resource_values.PreferredResourceValues"
    ]
    """<p> The list of preferred resources values that you want excluded from rightsizing recommendation candidates. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectivePreferredResource) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.preferred_resource_name

        out["name"] = (
            capo_compute_optimizer.types.preferred_resource_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "include_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["includeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_aws_json_1_0(
                value["include_list"]
            )
        )
    if "effective_include_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["effectiveIncludeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_aws_json_1_0(
                value["effective_include_list"]
            )
        )
    if "exclude_list" in value:
        import capo_compute_optimizer.types.preferred_resource_values

        out["excludeList"] = (
            capo_compute_optimizer.types.preferred_resource_values.serialize_aws_json_1_0(
                value["exclude_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EffectivePreferredResource:
    out: EffectivePreferredResource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_compute_optimizer.types.preferred_resource_name

        out["name"] = (
            capo_compute_optimizer.types.preferred_resource_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "includeList" in data:
        import capo_compute_optimizer.types.preferred_resource_values

        out["include_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_aws_json_1_0(
                data["includeList"]
            )
        )
    if "effectiveIncludeList" in data:
        import capo_compute_optimizer.types.preferred_resource_values

        out["effective_include_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_aws_json_1_0(
                data["effectiveIncludeList"]
            )
        )
    if "excludeList" in data:
        import capo_compute_optimizer.types.preferred_resource_values

        out["exclude_list"] = (
            capo_compute_optimizer.types.preferred_resource_values.deserialize_aws_json_1_0(
                data["excludeList"]
            )
        )
    return out
