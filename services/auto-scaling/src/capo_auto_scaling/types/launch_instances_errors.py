"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchInstancesErrors``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.launch_instances_error

LaunchInstancesErrors: TypeAlias = list[
    "capo_auto_scaling.types.launch_instances_error.LaunchInstancesError"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchInstancesErrors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.launch_instances_error

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.launch_instances_error.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LaunchInstancesErrors:
    import capo_auto_scaling.types.launch_instances_error

    out: LaunchInstancesErrors = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.launch_instances_error.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: LaunchInstancesErrors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.launch_instances_error

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.launch_instances_error.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LaunchInstancesErrors:
    import capo_auto_scaling.types.launch_instances_error

    out: LaunchInstancesErrors = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.launch_instances_error.deserialize_query(child)
        )
    return out
