"""Generated from Smithy shape ``com.amazonaws.glue#TransformEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.ml_user_data_encryption
    import capo_glue.types.name_string


class TransformEncryption(TypedDict, closed=True):
    ml_user_data_encryption: NotRequired[
        "capo_glue.types.ml_user_data_encryption.MLUserDataEncryption"
    ]
    """<p>An <code>MLUserDataEncryption</code> object containing the encryption mode and customer-provided KMS key ID.</p>"""
    task_run_security_configuration_name: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformEncryption) -> dict:
    out: dict = {}
    if "ml_user_data_encryption" in value:
        import capo_glue.types.ml_user_data_encryption

        out["MlUserDataEncryption"] = (
            capo_glue.types.ml_user_data_encryption.serialize_aws_json_1_1(
                value["ml_user_data_encryption"]
            )
        )
    if "task_run_security_configuration_name" in value:
        out["TaskRunSecurityConfigurationName"] = value[
            "task_run_security_configuration_name"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformEncryption:
    out: TransformEncryption = {}  # type: ignore[typeddict-item]
    if "MlUserDataEncryption" in data:
        import capo_glue.types.ml_user_data_encryption

        out["ml_user_data_encryption"] = (
            capo_glue.types.ml_user_data_encryption.deserialize_aws_json_1_1(
                data["MlUserDataEncryption"]
            )
        )
    if "TaskRunSecurityConfigurationName" in data:
        out["task_run_security_configuration_name"] = data[
            "TaskRunSecurityConfigurationName"
        ]
    return out
