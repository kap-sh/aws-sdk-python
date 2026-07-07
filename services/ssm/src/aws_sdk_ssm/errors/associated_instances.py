"""Generated from Smithy shape ``com.amazonaws.ssm#AssociatedInstances``."""

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import ServiceError


class AssociatedInstances_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedInstances_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedInstances_:
    out: AssociatedInstances_ = {}  # type: ignore[typeddict-item]
    return out


class AssociatedInstances(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AssociatedInstances``."""

    code: str | None = "AssociatedInstances"

    def __init__(self, data: AssociatedInstances_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociatedInstances",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AssociatedInstances":
        return cls(deserialize_aws_json_1_1(data))
