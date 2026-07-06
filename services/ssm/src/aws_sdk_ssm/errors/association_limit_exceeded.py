"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationLimitExceeded``."""

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import ServiceError


class AssociationLimitExceeded_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationLimitExceeded_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationLimitExceeded_:
    out: AssociationLimitExceeded_ = {}  # type: ignore[typeddict-item]
    return out


class AssociationLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AssociationLimitExceeded``."""

    code: str | None = "AssociationLimitExceeded"

    def __init__(self, data: AssociationLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociationLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AssociationLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
