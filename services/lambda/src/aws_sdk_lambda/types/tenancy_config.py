"""Generated from Smithy shape ``com.amazonaws.lambda#TenancyConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.tenant_isolation_mode


class TenancyConfig(TypedDict):
    tenant_isolation_mode: (
        "aws_sdk_lambda.types.tenant_isolation_mode.TenantIsolationMode"
    )
    """<p>Tenant isolation mode allows for invocation to be sent to a corresponding execution environment dedicated to a specific tenant ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TenancyConfig) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.tenant_isolation_mode

    out["TenantIsolationMode"] = (
        aws_sdk_lambda.types.tenant_isolation_mode.serialize_json(
            value["tenant_isolation_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> TenancyConfig:
    out: TenancyConfig = {}  # type: ignore[typeddict-item]
    if "TenantIsolationMode" in data:
        import aws_sdk_lambda.types.tenant_isolation_mode

        out["tenant_isolation_mode"] = (
            aws_sdk_lambda.types.tenant_isolation_mode.deserialize_json(
                data["TenantIsolationMode"]
            )
        )
    else:
        raise DeserializationError("TenancyConfig.tenant_isolation_mode required")
    return out
