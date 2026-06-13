"""Generated from Smithy shape ``com.amazonaws.eksauth#Subject``."""

from typing import TypedDict

from aws_sdk_eks_auth.errors import DeserializationError


class Subject(TypedDict):
    namespace: "str"
    """<p>The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the pods that use the service account must be in this namespace.</p>"""
    service_account: "str"
    """<p>The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subject) -> dict:
    out: dict = {}
    out["namespace"] = value["namespace"]
    out["serviceAccount"] = value["service_account"]
    return out


def deserialize_json(data: dict) -> Subject:
    out: Subject = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("Subject.namespace required")
    if "serviceAccount" in data:
        out["service_account"] = data["serviceAccount"]
    else:
        raise DeserializationError("Subject.service_account required")
    return out
