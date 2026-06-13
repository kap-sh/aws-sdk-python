"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_result
    import aws_sdk_bedrock_agentcore.errors.access_denied_exception
    import aws_sdk_bedrock_agentcore.errors.conflict_exception
    import aws_sdk_bedrock_agentcore.errors.internal_server_exception
    import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
    import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agentcore.errors.throttling_exception
    import aws_sdk_bedrock_agentcore.errors.validation_exception

class _CodeInterpreterStreamOutput_result(TypedDict):
    result: "aws_sdk_bedrock_agentcore.types.code_interpreter_result.CodeInterpreterResult"


class _CodeInterpreterStreamOutput_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException_"


class _CodeInterpreterStreamOutput_conflictException(TypedDict):
    conflictException: "aws_sdk_bedrock_agentcore.errors.conflict_exception.ConflictException_"


class _CodeInterpreterStreamOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _CodeInterpreterStreamOutput_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException_"


class _CodeInterpreterStreamOutput_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _CodeInterpreterStreamOutput_throttlingException(TypedDict):
    throttlingException: "aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException_"


class _CodeInterpreterStreamOutput_validationException(TypedDict):
    validationException: "aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException_"

CodeInterpreterStreamOutput: TypeAlias = _CodeInterpreterStreamOutput_result | _CodeInterpreterStreamOutput_accessDeniedException | _CodeInterpreterStreamOutput_conflictException | _CodeInterpreterStreamOutput_internalServerException | _CodeInterpreterStreamOutput_resourceNotFoundException | _CodeInterpreterStreamOutput_serviceQuotaExceededException | _CodeInterpreterStreamOutput_throttlingException | _CodeInterpreterStreamOutput_validationException

# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterStreamOutput) -> dict:
    if "result" in value:
        import aws_sdk_bedrock_agentcore.types.code_interpreter_result
        return {"result": aws_sdk_bedrock_agentcore.types.code_interpreter_result.serialize_json(value["result"])}
    elif "accessDeniedException" in value:
        import aws_sdk_bedrock_agentcore.errors.access_denied_exception
        return {"accessDeniedException": aws_sdk_bedrock_agentcore.errors.access_denied_exception.serialize_json(value["accessDeniedException"])}
    elif "conflictException" in value:
        import aws_sdk_bedrock_agentcore.errors.conflict_exception
        return {"conflictException": aws_sdk_bedrock_agentcore.errors.conflict_exception.serialize_json(value["conflictException"])}
    elif "internalServerException" in value:
        import aws_sdk_bedrock_agentcore.errors.internal_server_exception
        return {"internalServerException": aws_sdk_bedrock_agentcore.errors.internal_server_exception.serialize_json(value["internalServerException"])}
    elif "resourceNotFoundException" in value:
        import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
        return {"resourceNotFoundException": aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.serialize_json(value["resourceNotFoundException"])}
    elif "serviceQuotaExceededException" in value:
        import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
        return {"serviceQuotaExceededException": aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.serialize_json(value["serviceQuotaExceededException"])}
    elif "throttlingException" in value:
        import aws_sdk_bedrock_agentcore.errors.throttling_exception
        return {"throttlingException": aws_sdk_bedrock_agentcore.errors.throttling_exception.serialize_json(value["throttlingException"])}
    elif "validationException" in value:
        import aws_sdk_bedrock_agentcore.errors.validation_exception
        return {"validationException": aws_sdk_bedrock_agentcore.errors.validation_exception.serialize_json(value["validationException"])}
    else:
        raise SerializationError("CodeInterpreterStreamOutput: no variant present")


def deserialize_json(data: dict) -> CodeInterpreterStreamOutput:
    if "result" in data:
        import aws_sdk_bedrock_agentcore.types.code_interpreter_result
        return {"result": aws_sdk_bedrock_agentcore.types.code_interpreter_result.deserialize_json(data["result"])}
    elif "accessDeniedException" in data:
        import aws_sdk_bedrock_agentcore.errors.access_denied_exception
        return {"accessDeniedException": aws_sdk_bedrock_agentcore.errors.access_denied_exception.deserialize_json(data["accessDeniedException"])}
    elif "conflictException" in data:
        import aws_sdk_bedrock_agentcore.errors.conflict_exception
        return {"conflictException": aws_sdk_bedrock_agentcore.errors.conflict_exception.deserialize_json(data["conflictException"])}
    elif "internalServerException" in data:
        import aws_sdk_bedrock_agentcore.errors.internal_server_exception
        return {"internalServerException": aws_sdk_bedrock_agentcore.errors.internal_server_exception.deserialize_json(data["internalServerException"])}
    elif "resourceNotFoundException" in data:
        import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
        return {"resourceNotFoundException": aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.deserialize_json(data["resourceNotFoundException"])}
    elif "serviceQuotaExceededException" in data:
        import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
        return {"serviceQuotaExceededException": aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.deserialize_json(data["serviceQuotaExceededException"])}
    elif "throttlingException" in data:
        import aws_sdk_bedrock_agentcore.errors.throttling_exception
        return {"throttlingException": aws_sdk_bedrock_agentcore.errors.throttling_exception.deserialize_json(data["throttlingException"])}
    elif "validationException" in data:
        import aws_sdk_bedrock_agentcore.errors.validation_exception
        return {"validationException": aws_sdk_bedrock_agentcore.errors.validation_exception.deserialize_json(data["validationException"])}
    else:
        raise DeserializationError("CodeInterpreterStreamOutput: no recognized variant key")