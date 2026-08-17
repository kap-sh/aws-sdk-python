"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesLocalStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean


class ManagedInstancesLocalStorageConfiguration(TypedDict, closed=True):
    use_local_storage: "capo_ecs.types.boolean.Boolean"
    """<p>Use instance store volumes for data storage when available. EBS volumes are not provisioned for data storage. If the container instance has multiple instance store volumes, a single data volume is created. Consider defining instance store requirements using the <code>localStorage</code>, <code>localStorageTypes</code> and <code>totalLocalStorageGB</code> properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstancesLocalStorageConfiguration) -> dict:
    out: dict = {}
    out["useLocalStorage"] = value.get("use_local_storage", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedInstancesLocalStorageConfiguration:
    out: ManagedInstancesLocalStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("useLocalStorage") is not None:
        out["use_local_storage"] = data["useLocalStorage"]
    else:
        out["use_local_storage"] = False
    return out
