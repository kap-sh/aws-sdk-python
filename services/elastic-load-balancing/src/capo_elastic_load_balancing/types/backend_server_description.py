"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#BackendServerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.instance_port
    import capo_elastic_load_balancing.types.policy_names


class BackendServerDescription(TypedDict, closed=True):
    instance_port: NotRequired[
        "capo_elastic_load_balancing.types.instance_port.InstancePort"
    ]
    """<p>The port on which the EC2 instance is listening.</p>"""
    policy_names: NotRequired[
        "capo_elastic_load_balancing.types.policy_names.PolicyNames"
    ]
    """<p>The names of the policies enabled for the EC2 instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BackendServerDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_port" in value:
        pairs.append((f"{key_prefix}InstancePort", str(value["instance_port"])))
    if "policy_names" in value:
        import capo_elastic_load_balancing.types.policy_names

        capo_elastic_load_balancing.types.policy_names.serialize_query(
            value["policy_names"], pairs, f"{key_prefix}PolicyNames"
        )


def deserialize_query(el: Element) -> BackendServerDescription:
    out: BackendServerDescription = {}  # type: ignore[typeddict-item]
    child_instance_port = el.find("InstancePort")
    if child_instance_port is not None:
        out["instance_port"] = int(child_instance_port.text or "")
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_elastic_load_balancing.types.policy_names

        out["policy_names"] = (
            capo_elastic_load_balancing.types.policy_names.deserialize_query(
                child_policy_names
            )
        )
    return out
