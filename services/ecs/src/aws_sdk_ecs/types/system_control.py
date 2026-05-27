"""Generated from Smithy shape ``com.amazonaws.ecs#SystemControl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class SystemControl(TypedDict):
    namespace: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The namespaced kernel parameter to set a <code>value</code> for.</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The namespaced kernel parameter to set a <code>value</code> for.</p> <p>Valid IPC namespace values: <code>\"kernel.msgmax\" | \"kernel.msgmnb\" | \"kernel.msgmni\" | \"kernel.sem\" | \"kernel.shmall\" | \"kernel.shmmax\" | \"kernel.shmmni\" | \"kernel.shm_rmid_forced\"</code>, and <code>Sysctls</code> that start with <code>\"fs.mqueue.*\"</code> </p> <p>Valid network namespace values: <code>Sysctls</code> that start with <code>\"net.*\"</code>. Only namespaced <code>Sysctls</code> that exist within the container starting with \"net.* are accepted.</p> <p>All of these values are supported by Fargate.</p>"""
